import BlogCard from "../components/BlogCard.js"
export default{
    template:`
    <div class="p-4">
        <h1>Blogs List ❤</h1>
        <BlogCard v-for="blog in blogs" :key="blog.id" :title="blog.title" :date="blog.timestamp" :author_id="blog.user_id"></BlogCard>
    </div>
    `,
        //v-bind: to dynamically fetch data
        //<h2>{{$store.state.auth_token}}</h2>
        // <h3 v-for="blog in blogs">{{blog.title}}</h3>

    data(){
        //data is a function that returns an object
        return{
            blogs:[]
        }
    },
    methods:{

    },
    async mounted(){
        const res = await fetch(location.origin + '/api/blogs',{
            headers:{
                //"Authentication-Token":JSON.parse(localStorage.getItem('user')).token 
                // //instead of setting up from local storage now we can setup from vuex store
                "Authentication-Token":this.$store.state.auth_token
            }
        })
        this.blogs= await res.json()
    },
    //localising this blogcard component so that it can be only utilised in this file
    components:{
        BlogCard,
    } 
}