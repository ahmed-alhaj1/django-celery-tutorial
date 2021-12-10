import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Chat from '@/component/Chat'
import UserAuth from '@/component/UserAuth'
import { session } from 'electron'



Vue.use(Router)

const router =  new Router({
  routes: [
    {
      path: '/Chat',
      name: 'Chat',
      component: HelloWorld
    },
    {
      path : '/auth',
      name : '/UserAuth',
      components : UserAuth 
    }
  ]
})

router.beforeEach((to, from, next) => {
  if(sessionStorage.getItem('authToken') !== null || to.path === '/auth'){
    next()
  }else{
    next('/auth')
  }
})


export default router
