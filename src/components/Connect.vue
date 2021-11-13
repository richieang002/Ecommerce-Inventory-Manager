<template>
  <div class="connect">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Modak&display=swap" rel="stylesheet">
    <p class="title">Integrations</p>
    <button type="button" v-on:click="openModel()" class="btn3">Connect new platform</button>
    <div class="btn5">O</div>
    <div class="btn4">Connected </div>

    <div class="flexbox-container platform-body" style="display:flex; justify-content:space-evenly; margin-bottom:30px">
      <div style="margin:50px 50px 50px 50px">
        <b-container fluid class="p-4">
            <b-row>
                <b-col>
                  <div>
                    {{store.shop_url}}
                  </div>
                <b-img thumbnail fluid v-on:click="activeIntegration(1)" :src="imageslist.image1" v-bind:class="{ grayborder: isActive1, greenborder: active }"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid v-on:click="activeIntegration(2)" :src="imageslist.image2" v-bind:class="{ grayborder: isActive2 }"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid v-on:click="activeIntegration(3)" :src="imageslist.image3" v-bind:class="{ grayborder: isActive3 }"></b-img>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                <b-img thumbnail fluid v-on:click="activeIntegration(4)" :src="imageslist.image4" v-bind:class="{ grayborder: isActive4 }"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid v-on:click="activeIntegration(5)" :src="imageslist.image5" v-bind:class="{ grayborder: isActive5 }"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid v-on:click="activeIntegration(6)" :src="imageslist.image6" v-bind:class="{ grayborder: isActive6 }"></b-img>
                </b-col>
            </b-row>
        </b-container>
      </div>
    </div>
    <b-modal ref="my-modal" hide-footer title="Connect To Shop">
      <div class="d-block text-center">
        <div class="d-flex justify-content-center offtop">
          <b-form-input
          id="input-small"
          size="sm"
          placeholder="Store URL"
          type="text"
          style="width: 280px"
          trim
          v-model="shopURL"
          ></b-form-input>
        </div>
        <div>
          <span class="text-danger">{{msg}}</span>
        </div>
      </div>
      <div class="flexbox-container" style="display:flex; justify-content:space-between; margin-top:25px">
      <b-button class="mt-2" variant="outline-secondary" block @click="hideModal">Cancel</b-button>
      <b-button class="mt-2" variant="outline-danger" block @click="connect">Connect</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
import image1 from "./component_assets/shopify.png"
import image2 from "./component_assets/ebay.png"
import image3 from "./component_assets/shopee.png"
import image4 from "./component_assets/qoo.png"
import image5 from "./component_assets/taobao.png"
import image6 from "./component_assets/lazada.png"
import axios from './axios'

export default {
  name: 'Connect',
  data() {
    return {
        imageslist: { image1: image1, image2: image2, image3: image3, image4: image4, image5: image5, image6: image6 },
        isActive1: true,
        isActive2: false,
        isActive3: false,
        isActive4: false,
        isActive5: false,
        isActive6: false,
        active: false,
        shopURL: '',
        msg: '',
        store: {}
    }
  },
  props: {
    relative: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    activeIntegration(val){
      for(let i=1; i<7; i++){
        this[`isActive${i}`] = false
      }
      this[`isActive${val}`] = true
    },
    openModel(){
      this.$refs['my-modal'].show();
    },
    hideModal(){
      this.$refs['my-modal'].hide();
    },
    connect(){
      if(this.shopURL){
        window.location.href = 'http://localhost:8000/shopify/login/?shop='+this.shopURL
      }
      else{
        this.msg = 'Please enter shop url'
      }
    }
  },
  computed: {
    
  },
  async mounted() {
    let user = await localStorage.getItem('user')
    if(this.$route.query.access_code && this.$route.query.shop_url){
      try{
        await axios.post('shopify/shopify_shop/', {
            shop_url: this.$route.query.shop_url,
            access_code: this.$route.query.access_code,
            user: JSON.parse(user).pk
        })
        alert('shopify integration complete')
      }
      catch (e) {
        alert('shopify integration failed')
      }
      this.$router.push({ query: {} })
    }

    let stores = (await axios.get('shopify/shopify_shop/')).data
    stores.forEach(store => {
      console.log(store)
      if(store.user === JSON.parse(user).pk){
        this.store = store
        this.active = true
      }
    })
  }
// // start
//     connectbtn() {
//       this.$refs['my-modal'].show();
//     },
//     hideModal() {
//       this.$refs['my-modal'].hide();
//     },
//     connect() {
//       this.$refs['my-modal2'].show();
//     },
//     hideModal2() {
//       this.$refs['my-modal2'].hide();
//     },
//     confirm() {
//       this.$refs['my-modal'].hide();
//       this.$refs['my-modal2'].hide();
//     }
// // end 
  
}
</script>

<style scoped>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.title {
  text-align:left;
  font-family: 'Mulish', sans-serif;
  font-size: 20px;
}
.selection {
  border-style: solid;
  border-width: thin;
  border-color: lightgray;
}
.platform-body {
  border-style: solid;
  border-width: thin;
  border-color: lightgray;
}
.btn3 {
  padding: 3px 30px;
  font-size: 13px;
  background-color: #6670fa;
  color: rgb(255, 255, 255);
  border-radius: 5px;
  border: 0;
  position:absolute;
  margin-top: 10px;
  left: 270px;
}
.btn4 {
  padding: 5px 30px;
  font-size: 13px;
  color: rgb(0, 0, 0); 
  position:absolute;
  right: 20px;
  margin-top: 10px;
}
.btn5 {
  padding: 5px 30px;
  font-size: 13px;
  color: rgb(7, 219, 0); 
  position:absolute;
  right: 90px;
  font-family: 'Modak', cursive;
  margin-top: 10px;
}
.grayborder {
  border-style: solid;
  border-color: gray;
  border-width: medium;
}
.greenborder {
  border-style: solid;
  border-color: rgb(35, 255, 152);
  border-width: medium;
}
.offtop {
  margin-top: 10px;
}
.boxer {
  margin-top:15px;
  border-bottom: 1px solid rgb(189, 189, 189);
  padding-bottom:15px;
}
</style>
