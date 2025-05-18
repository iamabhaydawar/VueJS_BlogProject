import BlogsListPage from "../pages/BlogsListPage.js";
import LoginPage from "../pages/LoginPage.js";
import RegisterPage from "../pages/RegisterPage.js";
import BlogDisplayPage from "../pages/BlogDisplayPage.js";
import store from "./store.js";
import AdminDashboardPage from "../pages/AdminDashboardPage.js";
const Home ={
    template :`<h1>Home Page</h1>`
}

const routes =[
    {path:'/',component:Home},
    {path:'/login',component:LoginPage},
    {path:'/register',component:RegisterPage},
    //meta info required for navigation gaurds
    {path:'/feed',component:BlogsListPage, meta:{requiresLogin:true}},
    {path:'/blogs/:id',component:BlogDisplayPage, props:true, meta:{requiresLogin:true}},
    {path:'/admin-dashboard', component:AdminDashboardPage, meta:{requiresLogin:true, role:"admin"}}
]
// ,router.params.id
const router = new VueRouter({
    routes
})

//navigation gaurds this is for only frontend 
// // for backend we have auth_required 
//everytime we move from one route to another the view-routing should change accordingly
// logout should go back to front route again
router.beforeEach((to, from, next) => {
    
   //this checks if state is logged in or not
    //can match to mutliple components to.matched -array/list of objects
    // to - route going to 
    if(to.matched.some((record) => record.meta.requiresLogin)) {
        if(!store.state.loggedIn) {
            next({path: '/login'});
            return;
        }
    }//person is logged in but they are not authorised to access that specific role 
    if(to.meta.role && to.meta.role != store.state.role) { 
        alert('role not authorised');
        next({path: '/'});
        return;
    } 
   next();
})

export default router;