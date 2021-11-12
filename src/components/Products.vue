<template>
  <div class="overview">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <div class="display">
      <div class="flexbox-container" style="display:flex; justify-content:space-between; margin-top:25px">
        <div class="title-header" style="flex:1; text-align:left; margin-left:20px;">Products</div>
        <div class="main-user" style="flex:1; text-align:right; margin-right:20px;">{{username}} <b-avatar></b-avatar></div>
      </div>
      <div class="flexbox-container" style="display:flex; margin-top:30px; justify-content:center;">
        <div class="link2"><router-link to="/products/product" style="text-decoration: none;">Product</router-link></div>
      </div>
      <div style="margin-left:20px; margin-right:20px; margin-top:50px">
      <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Overview',
  data() {
    return {
        username:''
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
.inputst {
  font-size:13px;
  background-color: #f5f5f5;
  color: rgb(182, 182, 182);
  border: 0;
}
.offtop {
  margin-top: 40px;
  margin-left: 20px;
}
.offtop2 {
  margin-top: 20px;
}
.offtop3 {
  margin-top: 20px;
}
.v-sidebar-menu {
  color: rgb(128, 128, 128);
}
.v-sidebar-menu .vsm--list {
  text-align: center;
}
.display {
  margin-left: 240px;
}
.title-header {
  font-family: 'Mulish', sans-serif;
  font-size: 24px;
}
.link1 {
  font-family: 'Mulish', sans-serif;
  font-size: 20px;
  text-align: right;
}
.link2 {
  font-family: 'Mulish', sans-serif;
  font-size: 20px;
  text-align: left;
}
.router-link-active {
  color: #3751FF;
}
a {
  color: rgb(163, 163, 163);
}
</style>
