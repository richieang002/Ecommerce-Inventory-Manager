<template>
  <b-container fluid>
    <!-- User Interface controls -->
    <div id="searchBarContainer">
    <b-row >
    <b-col></b-col>
    <b-col></b-col>
      <b-col id="searchBar" lg="4" class="my-1">
        <b-form-group
          label=""
          label-for="filter-input"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          class="mb-0"
        >
          <b-input-group size="sm" class="mb-2">
            <b-input-group-prepend is-text>
            <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
        <b-form-input id="filter-input"
              v-model="filter"
              type="search"
              placeholder="Type to Search"></b-form-input>
              <!--<b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>-->
    </b-input-group>
        </b-form-group>
      </b-col>
    </b-row>
</div>
    <!-- Main table element -->
    <b-table
      :items="items"
      :fields="fields"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      :filter-included-fields="filterOn"
      stacked="md"
      show-empty
      small
      @filtered="onFiltered"
    >
      <template #cell(image)="row">
        <b-img class="myImage" fluid v-bind:src=row.item.image rounded="Rounded image" alt="image path" width="75">
        </b-img>
      </template>
      <template #cell(Delete)="row">
        <b-button size="sm" @click="edit(row.items, row.item, $event.target)" class="mr-1 btn-danger">
         Delete
        </b-button>
      </template>

 
    </b-table>

    <!-- Info modal -->
        <!-- Info modal -->
    <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">

     <template>
      <p>Do you want to delete this product?</p>
       <b-form-checkbox v-model="shopify">&nbsp;Shopify</b-form-checkbox>
       <div><span class="text-danger">{{msg}}</span></div>
    </template>

      <pre>{{ infoModal.Items }}</pre>
      <template #modal-footer="{ cancel}">
      <!-- Emulate built in modal footer ok and cancel button actions -->
      <b-button size="sm" variant="secondary" @click="cancel()">
        Cancel
      </b-button>
      <b-button size="sm" variant="danger" @click="delete_product">
        Delete
      </b-button>
    </template>
    </b-modal>
    <b-row>
    <b-col></b-col>
    <b-col></b-col>
    <b-col></b-col>
    
    <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          align="right"
          size="sm"
          class="my-0"
        ></b-pagination>
        </b-col>
        </b-row>
  </b-container>
</template>
<style scoped>

</style>
<script>
  import axios from "./axios";

  export default {
    data() {
      return {
        items: [],
        fields: ['image', 'title', 'platform','Collection',"Delete"],
        currentPage: 1,
        perPage: 5,
        //pageOptions: [5, 10, 15, { value: 100, text: "Show More" }],
        filter: null,
        filterOn: [],
        infoModal: {
          id: 'info-modal',
          title: '',
          content: ''
        },
        shopify: false,
        msg: '',
        selectedItem: {}
      }
    },
    computed: {
      rows() {
        return this.items.length
      },
      sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      }
    },
    mounted() {
      // Set the initial number of items
      this.totalRows = this.items.length
    },
    methods: {
      edit(items, item, button) {
        console.log(item)
        this.infoModal.title = `Delete: ${item.title}`
        this.infoModal.content = JSON.stringify(items, null, 2)
        this.msg = ''
        this.selectedItem = item
        this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      },
      async delete_product() {
        if(!this.shopify){
          this.msg = 'Please select platform to delete'
          return
        }
        try{
        await axios.post('shopify/product/delete/', {
          id: this.selectedItem.variant_id,
          product_id: this.selectedItem.id
        })
        this.items = this.items.filter(item => {
          return item.variant_id !== this.selectedItem.variant_id
        })
        alert('Update Success')
        this.$root.$emit('bv::hide::modal', this.infoModal.id)
      }
      catch (e) {
        console.log(e)
      }
      },
        resetInfoModal() {
        this.infoModal.title = ''
        this.infoModal.content = ''
      },
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
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