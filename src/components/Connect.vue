<template>
  <div class="connect">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Modak&display=swap" rel="stylesheet">
    <p class="title">Integrations</p>
    <button type="button" class="btn3" @click="connectbtn">Connect new platform</button>
    <div class="btn5">O</div>
    <div class="btn4">Connected</div>
    <div class="flexbox-container platform-body" style="display:flex; justify-content:space-evenly; margin-bottom:30px">
      <div style="margin:50px 50px 50px 50px">
        <b-container fluid class="p-4">
          <b-row>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image1" v-bind:class="{ greenborder: isActive1 }"></b-img>
            </b-col>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image2" v-bind:class="{ greenborder: isActive2 }"></b-img>
            </b-col>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image3" v-bind:class="{ greenborder: isActive3 }"></b-img>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image4" v-bind:class="{ greenborder: isActive4 }"></b-img>
            </b-col>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image5" v-bind:class="{ greenborder: isActive5 }"></b-img>
            </b-col>
            <b-col>
            <b-img thumbnail fluid :src="imageslist.image6" v-bind:class="{ greenborder: isActive6 }"></b-img>
            </b-col>
          </b-row>
        </b-container>
      </div>
    </div>
    <b-modal ref="my-modal" hide-footer title="New connection">
      <div class="d-block text-left" style="margin-left:10px">
        <b-dropdown id="dropdown-1" text="Platforms" class="md-2">
          <b-dropdown-item>Shopify</b-dropdown-item>
          <b-dropdown-item>Ebay</b-dropdown-item>
          <b-dropdown-item>Shopee</b-dropdown-item>
          <b-dropdown-item>Qoo10</b-dropdown-item>
          <b-dropdown-item>Taobao</b-dropdown-item>
          <b-dropdown-item>Lazada</b-dropdown-item>
        </b-dropdown>
        <div class="d-flex justify-content-left offtop">
          <b-form-group label="Access Token" label-for="input-acctoken" @submit.stop.prevent>
            <b-form-input
            class="accesstoken"
            id="input-acctoken" 
            size="sm"
            placeholder="Access Token" 
            type="number"
            style="width: 420px"
            trim
            ></b-form-input>
          </b-form-group>
        </div>
        <div class="d-flex justify-content-left offtop">
          <b-form-group label="App Key" label-for="input-appkey" @submit.stop.prevent>
            <b-form-input
            class="appkey"
            id="input-appkey" 
            size="sm"
            placeholder="App Key" 
            type="number"
            style="width: 420px"
            trim
            ></b-form-input>
          </b-form-group>
        </div>
      </div>
      <div class="flexbox-container" style="display:flex; justify-content:center; margin-top:25px">
      <b-button class="mt-2" variant="outline-secondary" block @click="hideModal">Cancel</b-button>
      <b-button class="mt-2" variant="outline-primary" block @click="connect" style="margin-left:40px">Connect</b-button>
      </div>
    </b-modal>
    <b-modal ref="my-modal2" hide-footer hide-header size="sm">
      <div class="d-block text-center">
        <div class="flexbox-container" style="flex-direction:column">
          <div class="boxer">Platform
            <div style="font-family: 'Mulish', sans-serif;"> {{ platformname }} </div>
          </div>
          <div class="boxer">Number of SKUs
            <div style="font-family: 'Mulish', sans-serif;"> {{ noSKU }} </div>
          </div>
          <div class="boxer">Accepted
            <div style="font-family: 'Mulish', sans-serif;"> {{ accepted }} </div>
          </div>
          <div class="boxer">Rejected
            <div style="font-family: 'Mulish', sans-serif;"> {{ rejected }} </div>
          </div>
        </div>
      </div>
      <div class="flexbox-container" style="display:flex; justify-content:center; margin-top:25px">
      <b-button class="mt-2" variant="outline-secondary" block @click="hideModal2">Back</b-button>
      <b-button class="mt-2" variant="outline-primary" block @click="confirm" style="margin-left:40px">Confirm</b-button>
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

export default {
  name: 'Connect',
  data() {
    return {
        imageslist: { image1: image1, image2: image2, image3: image3, image4: image4, image5: image5, image6: image6,},
        isActive1: true,
        isActive2: true,
        isActive3: false,
        isActive4: false,
        isActive5: false,
        isActive6: false,
        platformname: "Shopee",
        noSKU: "83",
        accepted: "83",
        rejected: "0",
    }
  },
  props: {
    relative: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    connectbtn() {
      this.$refs['my-modal'].show();
    },
    hideModal() {
      this.$refs['my-modal'].hide()
    },
    connect() {
      this.$refs['my-modal2'].show();
    },
    hideModal2() {
      this.$refs['my-modal2'].hide()
    },
    confirm() {
      this.$refs['my-modal'].hide()
      this.$refs['my-modal2'].hide()
    }
  }
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
