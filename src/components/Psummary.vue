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
      <template #cell(Edit)="row">
        <b-button size="sm" @click="edit(row.items, row.index, $event.target)" class="mr-1">
         Edit
        </b-button>
      </template>

 
    </b-table>

    <!-- Info modal -->
        <!-- Info modal -->
    <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">

     <template>
      <p>DUMMY TEXT DK EDIT WHAT</p>
    </template>

      <pre>{{ infoModal.Items }}</pre>
      <template #modal-footer="{ ok, cancel}">
      <!-- Emulate built in modal footer ok and cancel button actions -->
      <b-button size="sm" variant="success" @click="ok()">
        Save
      </b-button>
      <b-button size="sm" variant="danger" @click="cancel()">
        Discard
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
          :total-rows="totalRows"
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
        fields: ['image', 'title', 'platform','Collection',"Edit"],
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        //pageOptions: [5, 10, 15, { value: 100, text: "Show More" }],
        filter: null,
        filterOn: [],
        infoModal: {
          id: 'info-modal',
          title: '',
          content: ''
        }
      }
    },
    computed: {
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
      edit(items, index, button) {
        this.infoModal.title = `Edit: ${index}`
        this.infoModal.content = JSON.stringify(items, null, 2)
        this.$root.$emit('bv::show::modal', this.infoModal.id, button)
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