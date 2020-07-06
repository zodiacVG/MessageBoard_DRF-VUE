<template>
  <div id="main">
    <div class="touxiang">
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    </div>
    <div class="userinfo">
      <p id="username">{{note.username}}</p>
      <p id="committime">{{note.committime}}</p>
    </div>
    <div id="upvote" class="vote">
      <button class="el-icon-arrow-up" @click="upvoteit(note.commitid)"></button>
      <p>{{upvote}}</p>
    </div>
    <div id="dowmvote" class="vote">
      <button class="el-icon-arrow-down" @click="downvoteit(note.commitid)"></button>
      <p>{{downvote}}</p>
    </div>
    <div class="content">
      <p class="content">{{note.content}}</p>
    </div>
  </div>
</template>>

<script>
import axios from 'axios'

export default {
  name: 'showCard',
  data: function () {
    return {
      upvote: this.note.upvote,
      downvote: this.note.downvote,
      uptime: 0,   //限制点赞/点踩次数
      downtime: 0
    }
  },
  props: {
    note: {}
  },
  methods: {
    upvoteit(tochangeid) {
      if (this.uptime > 0) {
        alert('只能点赞一次')
        return
      }
      this.uptime = this.uptime + 1
      this.upvote = this.upvote + 1
      console.log(this.upvote)
      axios({
        method: 'post',
        url: 'http://localhost:8001/messageboard/updownvote/voteup/',
        data: {
          commitid: tochangeid
        }
      })    },
    downvoteit(tochangeid) {
      if (this.downtime > 0) {
        alert('只能点踩一次')
        return
      }
      this.downtime = this.downtime + 1
      this.downvote = this.downvote + 1
      console.log(this.downvote)
      axios({
        method: 'post',
        url: 'http://localhost:8001/messageboard/updownvote/votedown/',
        data: {
          commitid: tochangeid
        }
      })
    }

  }
}
</script>

<style scoped>
#main {
  margin-left: 20px;
  margin-bottom: 20px;
  background-color: antiquewhite;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}
.touxiang {
  margin-left: 20px;
  margin-top: 20px;
  float: left;
}
.userinfo {
  text-align: left;
  /* display: inline-block; */
  float: left;
  width: 300px;
  margin-left: 20px;
}
#username {
  height: 10px;
  font-weight: 800;
}
.vote {
  display: inline-block;
  margin-top: 10px;
}
.el-icon-arrow-up,
.el-icon-arrow-down {
  background-color: antiquewhite;
  border: 0ch;
}
.content {
  padding: 6px;
  text-align: left;
  width: 90%;
  background-color: aliceblue;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
</style>