<template>
  <div class="register">
    <img :src="image" width="300" height="80" class="offtop"> 
    <h6>Consolidating Your Ecommerce Needs</h6>
    <div  class="center-block text-center">
      <div class="d-flex justify-content-center offtop2">
        <b-form-input
        class="inputst offtop"
        id="input-small" 
        size="sm"
        :="firstname"
        placeholder="First Name" 
        type="text"
        style="width: 133px"
        trim
        ></b-form-input>
        <div class="empty">&ensp;&ensp;</div>
        <b-form-input
        class="inputst offtop"
        id="input-small" 
        size="sm"
        :="lastname"
        placeholder="Last Name" 
        type="text"
        style="width: 133px"
        trim
        ></b-form-input>
      </div>
    </div>
    <div class="d-flex justify-content-center offtop2">
        <b-form-input
        class="inputst"
        id="input-small" 
        size="sm"
        :="username"
        placeholder="User Name" 
        type="text"
        style="width: 280px"
        trim
        ></b-form-input>
    </div>
    <div class="d-flex justify-content-center offtop2">
        <b-form-input
        class="inputst"
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
    </div>
    <div class="d-flex justify-content-center offtop2">
        <b-form-input
        class="inputst"
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
    </div>
    <div  class="d-flex justify-content-center center-block text-center offtop3">
        <button class="btn1" @click="loginPage()">Cancel</button>
        <div class="empty">&ensp;&ensp;&ensp;</div>
        <button class="btn2" @click="signUp()">Sign Up</button>
    </div>
  </div>
</template>

<script>
import image from "./component_assets/group.png"

export default {
  name: 'Register',
  data() {
    return {
      image: image
    }
  },
  methods: {
    loginPage() {
      this.$router.push({ path: '/'})
    },
    signUp() {

    }
  }
}
</script>

<style scoped>
.inputst {
  font-size:13px;
  background-color: #f5f5f5;
  color: rgb(182, 182, 182);
  border: 0;
}
.offtop {
  margin-top: 40px;
}
.offtop2 {
  margin-top: 20px;
}
.offtop3 {
  margin-top: 20px;
}
.btn1 {
  padding: 5px 30px;
  font-size: 13px;
  background-color: #fa6666;
  color: rgb(255, 255, 255);
  border-radius: 5px;
  border: 0;
}
.btn2 {
  padding: 5px 50px;
  font-size: 13px;
  background-color: #6670fa;
  color: rgb(255, 255, 255);
  border-radius: 5px;
  border: 0;
}
</style>
