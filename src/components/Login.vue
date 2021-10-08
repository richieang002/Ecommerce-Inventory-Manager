<template>
  <div class="login">
    <b-container>
      <b-row>
        <img :src="image" width="300" height="80">
      </b-row> 
      <h6>{{ msg }}</h6>
      <div class="d-flex justify-content-center">
          <b-form-input
          class="loginemail"
          id="input-small" 
          size="sm"
          :="email"
          placeholder="Email Address" 
          type="email"
          state="emailState"
          style="width: 250px"
          aria-describedby="input-small-help input-small-feedback"
          trim
          ></b-form-input>
          
          <b-form-invalid-feedback id="input-small-feedback">
              Enter a valid email address
          </b-form-invalid-feedback>
      </div>
      <div class="d-flex justify-content-center">
          <b-form-input
          class="loginpw"
          id="input-small2"
          size="sm"
          :="password"
          placeholder="Password" 
          type="password"
          state="pwState"
          style="width: 250px"
          aria-describedby="input-small2-help input-small2-feedback"
          trim
          ></b-form-input>
          
          <b-form-invalid-feedback id="input-small2-feedback">
              Enter a valid password
          </b-form-invalid-feedback>
      </div>
      <div class="container" role="main">
          <div  class="center-block text-center">
              <button class="btn1">Create Account</button>
              <div class="empty">&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;</div>
              <button class="btn2">Forget Password</button>
          </div>
      </div>
      <div class="container" role="main">
          <div  class="center-block text-center">
              <button class="btn3">Log in</button>
          </div>
      </div>
    </b-container>
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
    props: {
        msg: String
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  text-align: center;
}
label {
  margin-bottom: 10px;
}
h5 {
  font-size:14px;
  height:8px;
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
.btn2 {
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
</style>
