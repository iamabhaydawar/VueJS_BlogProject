export default{
    props : ['title','author_id','date'],
    template:`
    <div class='jumbotron'>
        <h2>{{title}}</h2>
        <p>{{author_id}}</p>
        <hr>
        <p>Published:{{formattedDate}}</p>
    </div>
    `,
    computed:{
        formattedDate(){
            return new Date(this.date).toLocaleDateString(); //to make date human readable
        }
    }
}