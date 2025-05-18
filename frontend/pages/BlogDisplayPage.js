export default{
    props : ['id'],
    template:`
    <div>
        <h2>{{blog.title}}</h2>
        <img v-bind:src="blog.image_url" width='150'/>
        <p v-if="blog.timestamp">Published: {{ formattedDate }}</p>
        <p>{{blog.caption}}</p>
    
    </div>
    `,
    data(){
        return{
            blog:{},
        }
    },
    computed : {
        formattedDate() {
            return new Date(this.blog.timestamp).toLocaleDateString();
        }
    },   
    async mounted(){    
        const res = await fetch(`${location.origin}/api/blogs/${this.id}`,{
            headers :{
                'Authentication-Token':this.$store.state.auth_token
            }
        });
        if(res.ok){
            this.blog = await res.json();
        }
    }
}