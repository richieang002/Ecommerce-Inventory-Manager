<template>
  <div class="Summary">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <div id="rowDiv" class="row">
      <div id="lhsOuterDiv" class="col-md-8 box">
        <div class="col-md-8 box">
          <h3 id="header" style="font-size:20px; font-family: 'Mulish', sans-serif;">Featured Product</h3>
          <p id="timeDate" class="text-muted" style="font-size:14px">as of {{currentDateTime()}}</p>
          <b-img thumbnail fluid :src="imagetest"></b-img>
        </div>
        <!-- insert graph here-->
      </div>

      <div id="rhsOuterDiv" class="col-md-4">
        <div id="rhsRowDiv" class="row-md-3">
          <b-table id="table" sticky-header :items="items" head-variant="light"></b-table>
            <div id="rhsDiv"><div class="text-muted">Total Products</div>
                <p id="importedVal" class="txtfont">{{ items.dailyOrders }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Total Quantity</div>
                <p id="importedVal" class="txtfont">{{ items.weeklyOrders }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Platforms</div>
                <p id="importedVal" class="txtfont">{{ items.purchasePerHour }}</p>
                <hr class="my-3">
            </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.Summary{
  border: solid;
  border-width: thin;
  border-color: lightgray;
}
#lhsOuterDiv{
  padding-left:30px;
}
#header{
  text-align: left;
}
#timeDate{
  text-align:left;
  font-size:15px;
}
#rhsRowDiv{
  border-left-style: solid;
  border-width: thin;
  border-color: lightgray;
  margin-top: 0px;
}
#importedVal{
  font-size: 24px;
}
.txtfont{
  font-family: 'Mulish', sans-serif;
}


</style>
<script>
  export default {
    data() {
      return {
       items: { dailyOrders: '-', weeklyOrders: '-', purchasePerHour: '-'},
       imagetest: ""
      }
    },
    methods: {
      currentDateTime() {
        const current = new Date();
        const date = current.getFullYear()+'-'+(current.getMonth()+1)+'-'+current.getDate();
        const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
        const dateTime = date +' '+ time;
        
        return dateTime;
      }
    },
    created() {
      this.username = JSON.parse(localStorage.getItem('user')).username
    }
  }
</script>