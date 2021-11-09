<template>
  <form @submit.prevent="">
  <div class="login">
    <img src="./component_assets/group.png" width="300" height="80" class="offtop"> 
    <h6>Consolidating Your Ecommerce Needs</h6>
    <div class="d-flex justify-content-center offtop">
      <b-form-input
      class="loginemail"
      id="input-small" 
      size="sm"
      placeholder="Username"
      type="text"
      style="width: 280px"
      trim
      v-model="username"
      ></b-form-input>
    </div>
    <div v-if="sent"><span>Please check your email for password.</span></div>
        <ul class="text-danger mt-2"><li v-for="(m, index) in msg" :key="index">{{ m }}</li></ul>

    <div  class="center-block text-center">
      <button class="btn1" @click="submit('register')">Create Account</button>
      <div class="empty">&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</div>
      <button class="btn1" @click="submit('login')">Log In</button>
    </div>
    <div  class="center-block text-center">
      <button class="btn3 offtop2" @click="submit('forget')">Send Password</button>
    </div>
  </div>
  </form>
</template>

<script>
import axios from 'axios'
  
  export default {
    name: 'ForgetPassword',
    computed: {
      
    },
    data() {
      return {
        username: '',
        msg: '',
        sent: false,
      }
    },
    methods: {
      async submit(action) {
        if (action == 'register') {
          this.$router.push({ path: '/register'})
        }
        else if (action == 'login') {
          this.$router.push({ path: '/'})
        }
        else if (action == 'forget') {
          try{
            await axios.post('password-reset/', {
            username: this.username
            });
            this.sent = true
          }
          catch (error) {
            this.msg = Object.values(error.response.data).flat()
          }
        }
      }
    }
  }
</script>

<style scoped>
body {
  text-align: center;
}

.loginpw {
  font-size:13px;
  background-color: #f5f5f5;
  color: rgb(182, 182, 182);
  border: 0;
}
.loginemail {
  font-size:13px;
  background-color: #f5f5f5;
  color: rgb(182, 182, 182);
  border: 0;
}
.btn1 {
  margin-top: 10px;
  padding: 5px 15px;
  font-size:12px;
  display: inline-block;
  background-color: #ffffff;
  color: rgb(109, 109, 109);
  border: 0;
}
.btn3 {
  padding: 5px 50px;
  font-size: 13px;
  background-color: #6670fa;
  color: rgb(255, 255, 255);
  border-radius: 5px;
  border: 0;
}
.empty {
  white-space: nowrap;
  display: inline-block;
}
.offtop {
  margin-top: 80px;
}
.offtop2 {
  margin-top: 20px;
}
</style>
