<template>
  <div class="overview">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <div class="display">
      <div class="flexbox-container" style="display:flex; justify-content:space-between; margin-top:25px">
        <div class="title-header" style="flex:1; text-align:left; margin-left:20px;">Overview</div>
        <div class="main-user" style="flex:1; text-align:right; margin-right:20px;">{{username}} <b-avatar></b-avatar></div>
      </div>
      <div style="margin-left:20px; margin-right:20px; margin-top:20px">
        <b-container fluid class="p-4">
          <b-row>
            <b-col>
              <b-card sub-title="Unfufilled" >
                <b-card-text class="qtytext">{{ unfulfilled }}</b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card sub-title="Overdue">
                <b-card-text class="qtytext">{{ overdue }}</b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card sub-title="Shipped">
                <b-card-text class="qtytext">{{ shipped }}</b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card sub-title="Closed">
                <b-card-text class="qtytext">{{ closed }}</b-card-text>
              </b-card>
            </b-col>
          </b-row>
        </b-container>
        <div class="Summary">
          <div id="rowDiv" class="row">
            <div id="lhsOuterDiv" class="col-md-8 box">
              <div class="col-md-8 box">
                <h3 id="header" style="font-size:20px; font-family: 'Mulish', sans-serif;">Today's trends</h3>
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
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Overview',
  data() {
    return {
        username: '',
        items: { dailyOrders: 'asd', weeklyOrders: '123', purchasePerHour: '222', revPerDay: '123',  netRev: '567'},
        unfulfilled: '60',
        overdue: '30',
        shipped: '43',
        closed: '367'
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
  props: {
    relative: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    
  },
  created() {
    this.username = JSON.parse(localStorage.getItem('user')).username
  }
}
</script>

<style scoped>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.v-sidebar-menu {
  color: rgb(128, 128, 128);
}
.v-sidebar-menu .vsm--list {
  text-align: center;
}
#id {
  background-color: #F7F8FC;
}
.display {
  margin-left: 240px;
}
.title-header {
  font-family: 'Mulish', sans-serif;
  font-size: 24px;
}
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
.qtytext{
  color: black;
  font-size: 40px;
  font-family: 'Mulish', sans-serif;
}
.txtfont{
  font-family: 'Mulish', sans-serif;
}
</style>
