<template>
  <div class="user">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css">
    <b-button class="button12" block @click="logoutbtn">Logout</b-button>
    <sidebar-menu :menu="menu" width="240px" hideToggle="true">
      <div slot="header" class="offtop">
        <b-avatar variant="primary" style="background-color:#3751FF;" text="L" size="md"></b-avatar>
        &ensp;{{username}}'s Store
      </div>
    </sidebar-menu>
    <b-modal ref="my-modal" hide-footer title="Logout screen">
      <div class="d-block text-center">
        <h4>Are you sure you want to log out?</h4>
      </div>
      <div class="flexbox-container" style="display:flex; justify-content:space-between; margin-top:25px">
      <b-button class="mt-2" variant="outline-secondary" block @click="hideModal">Cancel</b-button>
      <b-button class="mt-2" variant="outline-danger" block @click="logoutfn">Logout</b-button>
      </div>
    </b-modal>
    <router-view></router-view>
  </div>
</template>

<script>  

export default {
  name: 'User',
  data() {
    return {
      username: '',
        menu: [
            {
            header: 'Main Navigation',
            hiddenOnCollapse: false
            },
            {
            href: '/import/connect',
            title: 'Import / Export',
            icon: 'fa fa-forward'
            },
            {
            href: '/products/product',
            title: 'Products',
            icon: 'fa fa-adjust'
            },
            {
            href: '/platforms/psummary',
            title: 'Platforms',
            icon: 'fa fa-users'
            },
        ]
    }
  },
  props: {
    relative: {
      type: Boolean,
      default: true,
    },
    hideToggle: {
      type: Boolean,
      default: true
    },
    disableHover: {
      type: Boolean,
      default: true
    },
    collapsed: {
      type: Boolean,
      default: false
    },
  },
  created() {
    this.username = JSON.parse(localStorage.getItem('user')).username
  },
  methods: {
    logoutbtn() {
      this.$refs['my-modal'].show();
    },
    hideModal() {
        this.$refs['my-modal'].hide()
    },
    async logoutfn() {
      await localStorage.removeItem('token');
      await localStorage.removeItem('user');
      this.$router.push({ path: '/'});
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
  color: rgb(255, 254, 254);
  background-color: #313131;
}
.v-sidebar-menu .vsm_expanded .vsm--icon {
  background-color: #272727;
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
.button12 {
  position: absolute;
  bottom: 0px;
  z-index: 1000;
  left: 0;
  background-color: #313131;
  width: 240px;
  position:fixed;
  border-top-style: thin;
  border-top-color: #4d4d4d;
  border-left-style: none;
  border-right-style: none;
  border-bottom-style: none;
}
</style>
