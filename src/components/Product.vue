<template>
  <div class="Products">
    <div class="row">
<div class="col-md-8 box">
    <b-table
      hover 
      :items="items"
      :fields="fields"
      :select-mode="selectMode"
      responsive="sm"
      ref="selectableTable"
      selectable
      @row-selected="onRowSelected"
      
    >
      <!-- Example scoped slot for select state illustrative purposes -->
      <template #cell(image)="row">
        <b-img class="myImage" fluid v-bind:src=row.item.image rounded="Rounded image" alt="image path" width="75">
        </b-img>
      </template>
      <template #cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>
    </b-table>
</div>
    <div class="col-md-4">
          <div class="row">
            <div><div class="text-muted">Item</div>
              <div v-if="selected.length === 0" class="text-muted">No Rows Selected </div>
                <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.title }}</p>
                <!--<b-icon icon="search"></b-icon> -->
                <hr class="my-3">
                
            </div>
            <div><div class="text-muted">SKU</div>
              <div v-if="selected.length === 0" class="text-muted">No Rows Selected</div>
                <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.SKU }}</p>
                <hr class="my-3">
            </div>
            <div><div class="text-muted">Quantity</div>
              <div v-if="selected.length === 0" class="text-muted">No Rows Selected</div>
                <b-form-input
                  v-for="selected in selected" :key="selected"
                  id="input-small2"
                  size="sm"
                  placeholder="Quantity"
                  type="text"
                  trim
                  v-model="quantity"
                ></b-form-input>
                <hr class="my-3">
            </div>
            <div><div class="text-muted">Platforms</div>
              <div v-if="selected.length === 0" class="text-muted">No Rows Selected</div>
              <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.platform }}</p>
              <button v-if="selected.length" type="button" class="btn btn-primary" v-on:click="updateProductQuantity(selected[0])" >Update</button>
            </div>
          </div>
          </div>
          </div>
    <!--<p>
      Selected Rows:<br>
      {{ selected }}
    </p>-->
  </div>
</template>
<style scoped>
.Products{
  border: solid;
  border-width: thin;
  border-color: lightgray;
  padding: 20px;
}
.col-md-4{
  border-left-style: solid;
  border-width: thin;
  border-color: lightgray;
}
#importedVal{
  font-size: 30px;
}

</style>
<script>
  import axios from "./axios";

  export default {
    data() {
      return {
        fields: ['image', 'title', 'Tags'],
        items: [],
        selectMode: 'single',
        selected: [],
        quantity: 0,
        msg: '',
      }
    },
    methods: {
      onRowSelected(items) {
        this.selected = items
        this.quantity = items[0].inventory_quantity
      },
      async updateProductQuantity(product){
        try{
        (await axios.post('shopify/product/update/', {
          id: product.inventory_item_id,
          quantity: this.quantity
        })).data
        this.items.forEach(item => {
          if(item.variant_id===product.variant_id){
            item.inventory_quantity = this.quantity
          }
        })
        alert('Update Success')
      }
      catch (e) {
        console.log(e)
      }
      }
    },
    async created() {
      try{
        let response = (await axios.get('shopify/products/')).data
        this.items = response.products
      }
      catch (e) {
        console.log(e)
      }
    }
  }
</script>