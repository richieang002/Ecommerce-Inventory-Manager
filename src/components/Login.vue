<template>
  <form @submit.prevent="handleSubmit">
  <div class="login">
    <img src="./component_assets/group.png" width="300" height="80" class="offtop"> 
    <h6>Consolidating Your Ecommerce Needs</h6>
    <div class="d-flex justify-content-center offtop">
      <b-form-input
      class="loginemail"
      id="input-small" 
      size="sm"
      placeholder="Email Address" 
      type="email"
      style="width: 280px"
      trim
      v-model="email"
      ></b-form-input>
    </div>

    <div class="d-flex justify-content-center offtop2">
      <b-form-input
      class="loginpw"
      id="input-small2"
      size="sm"
      placeholder="Password" 
      type="password"
      style="width: 280px"
      trim
      v-model="password"
      ></b-form-input>
    </div>
    <div  class="center-block text-center">
      <button class="btn1" @click="registerPage()">Create Account</button>
      <div class="empty">&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</div>
      <button class="btn1">Forget Password</button>
    </div>
    <div  class="center-block text-center">
      <button class="btn3 offtop2" @click="finishLogin()">Log in</button>
    </div>
  </div>
  </form>
</template>

<script>
import axios from 'axios'
  
  export default {
    name: 'Login',
    computed: {
      
    },
    data() {
      return {
        email: '',
        password: ''
      }
    },
    methods: {
      registerPage() {
        this.$router.push({ path: '/register'})
      },
      // finishLogin() {
      //   this.$router.push({ path: '/user'})
      // },
      async handleSubmit() {
        const response = await axios.post('login', {
          email: this.email,
          password: this.password
        });

        localStorage.setItem('token', response.data.token);

        this.$router.push({ path: '/user'});
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
