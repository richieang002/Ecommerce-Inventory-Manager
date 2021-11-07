<template>
  <form @submit.prevent="">
  <div class="register">
    <img src="./component_assets/group.png" width="300" height="80" class="offtop"> 
    <h6>Consolidating Your Ecommerce Needs</h6>
    <div  class="center-block text-center">
      <div class="d-flex justify-content-center offtop2">
        
        <b-form-input
        class="inputst offtop"
        id="input-small1" 
        size="sm"
        placeholder="First Name" 
        type="text"
        style="width: 133px"
        trim
        v-model="firstname"
        ></b-form-input>

        <div class="empty">&ensp;&ensp;</div>
        
        <b-form-input
        class="inputst offtop"
        id="input-small2" 
        size="sm"
        placeholder="Last Name" 
        type="text"
        style="width: 133px"
        trim
        v-model="lastname"
        ></b-form-input>

      </div>
    </div>

    <div class="d-flex justify-content-center offtop2">
      <div role="group">
        
        <b-form-input
        class="inputst"
        id="input-small3" 
        size="sm"
        :state="unameState"
        aria-describedby="input-live-feedback"
        placeholder="User Name" 
        type="text"
        style="width: 280px"
        trim
        v-model="username"
        ></b-form-input>

        <b-form-invalid-feedback id="input-live-feedback"></b-form-invalid-feedback>

      </div>
    </div>

    <div class="d-flex justify-content-center offtop2">
      <div role="group">

        <b-form-input
        class="inputst"
        id="input-small4" 
        size="sm"
        :state="emailState"
        aria-describedby="input-live-feedback2"
        placeholder="Email Address" 
        type="email"
        style="width: 280px"
        trim
        v-model="email"
        ></b-form-input>

        <b-form-invalid-feedback id="input-live-feedback2"></b-form-invalid-feedback>

      </div>
    </div>

    <div class="d-flex justify-content-center offtop2">
      <div role="group">
      
        <b-form-input
        class="inputst"
        id="input-small5"
        size="sm"
        :state="pw1State"
        aria-describedby="input-live-feedback3"
        placeholder="Password" 
        type="password"
        style="width: 280px"
        trim
        v-model="password1"
        ></b-form-input>

        <b-form-invalid-feedback id="input-live-feedback3"></b-form-invalid-feedback>

      </div>
    </div>

    <div class="d-flex justify-content-center offtop2">
      <div role="group">

        <b-form-input
        class="inputst"
        id="input-small5"
        size="sm"
        :state="pw2State"
        aria-describedby="input-live-feedback3"
        placeholder="Confirm Password"
        type="password"
        style="width: 280px"
        trim
        v-model="password2"
        ></b-form-input>

        <b-form-invalid-feedback id="input-live-feedback3"></b-form-invalid-feedback>

      </div>
    </div>

    <ul class="text-danger mt-2"><li v-for="(m, index) in msg" :key="index">{{ m }}</li></ul>

    <div  class="d-flex justify-content-center center-block text-center offtop3">
      <button class="btn1" @click="submit('returnLogin')">Cancel</button>

      <div class="empty">&ensp;&ensp;&ensp;</div>

      <button class="btn2" @click="submit('signUp')">Sign Up</button>
    </div>
  
  </div>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Register',
  data() {
    return {
      firstname: '',
      lastname: '',
      email: '',
      username: '',
      password1: '',
      password2: '',
      msg: []
    }
  },
  methods: {
    async submit(action) {
      if (action == 'returnLogin') {
        this.$router.push({ path: '/'})
      }
      else if (action == 'signUp') {
        try{
          this.msg = []
          await axios.post('auth/register/', {
            firstname: this.firstname,
            lastname: this.lastname,
            email: this.email,
            username: this.username,
            password1: this.password1,
            password2: this.password2
          });
          return this.$router.push({ path: '/user'});
        }
        catch (error) {
          this.msg = Object.values(error.response.data).flat()
        }
      }
    }
  },
  computed: {
    emailState() {
        return this.email.length == 0 ? false : null
    },
    unameState() {
        return this.username.length == 0 ? false : null
    },
    pw1State() {
        return this.password1.length == 0 ? false : null
    },
    pw2State() {
        return this.password1.length == 0 ? false : null
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
