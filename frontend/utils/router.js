const Home ={
    template :`<h1>Home Page</h1>`
}
import BlogsListPage from "../pages/BlogsListPage.js";
import LoginPage from "../pages/LoginPage.js";
import RegisterPage from "../pages/RegisterPage.js";

const routes =[
    {path:'/',component:Home},
    {path:'/login',component:LoginPage},
    {path:'/register',component:RegisterPage},
    {path:'/feed',component:BlogsListPage}
]

const router = new VueRouter({
    routes
})
export default router;