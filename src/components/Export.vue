<template>
  <div class="connect">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Modak&display=swap" rel="stylesheet">
    <p class="title">Select platform to export data to file</p>
    <div class="flexbox-container platform-body" style="display:flex; justify-content:space-evenly; margin-bottom:30px">
        <div style="margin:50px 50px 50px 50px">
        <b-container fluid class="p-4">
            <b-row>
                <b-col>
                <b-img thumbnail fluid :src="image1" class="green-border"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid :src="image2" class="green-border"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid :src="image3" class="green-border"></b-img>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                <b-img thumbnail fluid :src="image4" class="green-border"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid :src="image5" class="green-border"></b-img>
                </b-col>
                <b-col>
                <b-img thumbnail fluid :src="image6" class="green-border"></b-img>
                </b-col>
            </b-row>
        </b-container>
        </div>
    </div>
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
        image1: image1,
        image2: image2,
        image3: image3,
        image4: image4,
        image5: image5,
        image6: image6,
    }
  },
  props: {
    relative: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    
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
.green-border {
  border-style: solid;
  border-color: rgb(0, 21, 88);
  border-width: medium;
}
</style>
