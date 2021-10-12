<template>
  <div class="login">
    <img :src="image" width="300" height="80" class="offtop"> 
    <h6>Consolidating Your Ecommerce Needs</h6>
    <div class="d-flex justify-content-center offtop">
      <b-form-input
      class="loginemail"
      id="input-small" 
      size="sm"
      :="email"
      placeholder="Email Address" 
      type="email"
      state="emailState"
      style="width: 280px"
      aria-describedby="input-small-help input-small-feedback"
      trim
      ></b-form-input>
      
      <b-form-invalid-feedback id="input-small-feedback">
          Enter a valid email address
      </b-form-invalid-feedback>
    </div>
    <div class="d-flex justify-content-center offtop2">
      <b-form-input
      class="loginpw"
      id="input-small2"
      size="sm"
      :="password"
      placeholder="Password" 
      type="password"
      state="pwState"
      style="width: 280px"
      aria-describedby="input-small2-help input-small2-feedback"
      trim
      ></b-form-input>
      
      <b-form-invalid-feedback id="input-small2-feedback">
          Enter a valid password
      </b-form-invalid-feedback>
    </div>
    <div  class="center-block text-center">
      <button class="btn1" @click="registerPage()">Create Account</button>
      <div class="empty">&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</div>
      <button class="btn1">Forget Password</button>
    </div>
    <div  class="center-block text-center">
      <button class="btn3 offtop2">Log in</button>
    </div>
  </div>
</template>

<script>
import image from "./component_assets/group.png"
  
  export default {
    name: 'Login',
    computed: {
      emailState() {
        let str = this.email
        return str.includes("@") ? true : false
      },
      pwState() {
        let str = this.password
        return str.includes("@") ? true : false
      }
    },
    data() {
      return {
        image: image
      }
    },
    methods: {
      registerPage() {
        this.$router.push({ path: '/register'})
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
