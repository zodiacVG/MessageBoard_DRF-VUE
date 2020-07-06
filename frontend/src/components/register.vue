<template>
  <div class="main">
    <div class="logbar">
      <el-form ref="form" :model="form" label-width="80px">
        <el-input v-model="form.username" placeholder="请输入用户名" class="input"></el-input>
        <el-input placeholder="（不能与用户名重复）请输入密码" v-model="form.password" show-password class="input"></el-input>
        <el-button type="primary" @click="onSubmit">注册</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'loginbar',
  data: function () {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit() {
      axios.post('http://localhost:8001/auth/users/', {
        username: this.form.username,
        password: this.form.password
      })
        .then(res => {
          console.log(res)
          alert('注册成功！请登录！')
        })
        .catch(err => {
          console.log('error')
          console.error(err);
          alert('注册失败，密码过于简单！')
        })
      console.log(this.form)
    this.$emit('newuser',this.form)
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
.el-avatar{
  size: 50;
}
</style>


