<template>
  <div class="home">
    <el-row>
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <el-divider content-position="center" id="firstdevider">留言</el-divider>
          <el-input v-model="content" placeholder="请输入留言(如未登录以游客身份)" id="contentinput" ref="messageform"></el-input>
          <el-button @click="submitNote();resetForm()" type="primary" icon="el-icon-edit">发布留言</el-button>
          <el-divider content-position="center" v-if="this.username===''">登录</el-divider>
          <loginbar id="loginbar" @loginsuccess="secclogin"></loginbar>
          <el-divider content-position="center">注册</el-divider>
          <register id="registerbar"></register>
        </div>
      </el-col>
      <el-col :span="16">
        <div class="grid-content bg-purple-light" :key="key">
          <showCard v-for="note in notes" :key="note.commitid" :note="note"></showCard>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// @ is an alias to /src
import showCard from '../components/showCard'
import loginbar from '../components/loginbar'
import register from '../components/register'
import axios from 'axios'

export default {
  name: 'Home',
  data: function () {
    return {
      notes: [],
      content: '',
      username: '',
      auth_token: '',
      key: 0
    }
  },
  components: {
    showCard,
    loginbar,
    register
  },
  mounted: function () {
    console.log('been called')
    axios.get('http://localhost:8001/messageboard/notes/')
      .then((response) => {
        this.notes = response.data
        console.log(response)
      })
  },
  methods: {
    resetForm() {
      this.content=''
    },
    secclogin: function (value) {
      console.log('传过来的value')
      console.log(value)
      console.log('传过来的value')
      this.username = value.username
      this.auth_token = value.auth_token
    },
    submitNote: function () {
      alert('发布成功')
      if (this.username === '') {
        axios.post('http://localhost:8001/messageboard/notes/', {
          content: this.content
        }).then((response) => {
          console.log(response)
        })      }
      else {
        axios.post('http://localhost:8001/messageboard/notes/', {
          username: this.username,
          content: this.content
        }).then((response) => {
          console.log(response)
        })
      }
      axios.get('http://localhost:8001/messageboard/notes/')
        .then((response) => {
          this.notes = response.data
          console.log(response)
        })
      this.key += 1
    }
  },

}
</script>

<style scoped>
.home {
  margin-left: 20%;
  margin-right: 20%;
}
.el-input {
  margin-top: 20px;
  margin-bottom: 20px;
}
.el-divider {
  margin-top: 60px;
}
.el-button {
  size: "medium";
  background-color: #67c23a;
  border: 0;
}
#loginbar {
  margin-top: 0;
}
#registerbar {
  margin-top: 20px;
}
#firstdevider {
  margin-top: 20px;
}
</style>
