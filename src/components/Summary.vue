<template>
  <div class="Summary">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <div id="rowDiv" class="row">
      <div id="lhsOuterDiv" class="col-md-8 box">
        <div class="col-md-8 box">
          <h3 id="header" style="font-size:20px; font-family: 'Mulish', sans-serif;">Best selling product</h3>
          <p id="timeDate" class="text-muted" style="font-size:14px">as of {{currentDateTime()}}</p>
        </div>
        <!-- insert graph here-->
      </div>

      <div id="rhsOuterDiv" class="col-md-4">
        <div id="rhsRowDiv" class="row-md-3">
          <b-table id="table" sticky-header :items="items" head-variant="light"></b-table>
            <div id="rhsDiv"><div class="text-muted">Daily Orders</div>
                <p id="importedVal" class="txtfont">{{ items.dailyOrders }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Weekly Orders</div>
                <p id="importedVal" class="txtfont">{{ items.weeklyOrders }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Purchases / Hours</div>
                <p id="importedVal" class="txtfont">{{ items.purchasePerHour }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Revenue / Day</div>
                <p id="importedVal" class="txtfont">{{ items.revPerDay }}</p>
                <hr class="my-3">
            </div>
            <div id="rhsDiv"><div class="text-muted">Net Revenue After Logistics</div>
                <p id="importedVal" class="txtfont">{{ items.netRev }}</p>
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
       items: { dailyOrders: 'asd', weeklyOrders: '123', purchasePerHour: '222', revPerDay: '123',  netRev: '567'}
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
    }
  }
</script>