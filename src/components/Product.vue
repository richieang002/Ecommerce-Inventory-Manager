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
                <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.Item }}</p>
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
                <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.Quantity }}</p>
                <hr class="my-3">
            </div>
            <div><div class="text-muted">Platforms</div>
              <div v-if="selected.length === 0" class="text-muted">No Rows Selected</div>
              <p id="importedVal" v-for="selected in selected" :key="selected">{{ selected.Platform }}</p>
              <button type="button" class="btn btn-primary">Update</button>
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
  export default {
    data() {
      return {
        fields: ['Image', 'Item', 'Tags'],
        items: [
          { Image: 'file/path', Item: 'Item Name1', Tags: 'A B' , Quantity: 10, SKU:'itemSKU1', Platform:'platformA , PlatformE, PlatformF'},
          { Image: 'file/path', Item: 'Item Name2', Tags: 'A B' , Quantity: 10, SKU:'itemSKU2', Platform:'platformB'},
          { Image: 'file/path', Item: 'Item Name3', Tags: 'A B' , Quantity: 10, SKU:'itemSKU3', Platform:'platformC'},
          { Image: 'file/path', Item: 'Item Name4', Tags: 'A B' , Quantity: 10, SKU:'itemSKU4', Platform:'platformD'}
        ],
        selectMode: 'single',
        selected: []
      }
    },
    methods: {
      onRowSelected(items) {
        this.selected = items
      }
    }
  }
</script>