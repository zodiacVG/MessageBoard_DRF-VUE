<template>
  <div class="main">
    <div class="logbar" v-if="logflag===false">
      <el-form ref="form" :model="form" label-width="80px">
        <el-input v-model="form.username" placeholder="请输入用户名" class="input"></el-input>
        <el-input placeholder="请输入密码" v-model="form.password" show-password class="input"></el-input>
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form>
    </div>
    <div class="loginfo" v-if="logflag===true">
      <el-avatar icon="el-icon-user-solid"></el-avatar>
      <h2 id="usernameafterlog">{{this.form.username}}</h2>
      <el-button type="primary" @click="logout">注销</el-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'loginbar',
  data: function () {
    return {
      logflag: false,   //控制登陆框是否显示
      form: {
        auth_token: '',
        username: '',
        password: ''
      },
    }
  },
  methods: {
    logout() {
      alert('注销成功')
      location.reload();
    },
    onSubmit() {
      axios.post('http://localhost:8001/auth/token/login/', {
        username: this.form.username,
        password: this.form.password
      })
        .then(res => {
          console.log('is empty?')
          console.log(res.data.auth_token)
          this.form.auth_token = res.data.auth_token;
          alert('登陆成功')
          this.$emit('loginsuccess', this.form)
          this.logflag = true;
        })
        .catch(err => {
          console.log('error')
          console.error(err);
          alert('登陆失败11')
        })
      console.log(this.form)
    }
  }
}
</script>
    
<style scoped>
.input {
  margin-bottom: 10px;
}
el-button {
  background-color: aliceblue;
}
.el-avatar {
  size: 50;
}
.loginfo {
  margin-top: 40px;
}
</style>


