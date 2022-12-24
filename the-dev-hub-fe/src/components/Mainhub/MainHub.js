import React, { useEffect, useState } from 'react'
import axios from 'axios'

const MainHub = () => {
    const [allPostings, setAllPostings] = useState()
    const[updatePost, setUpdatePost]= useState({
        title: "",
        company: "",
        posted: Date,
        url: ""
    })

    const getAllPostings = () =>{
        axios
        .get('http://localhost:8000/api/postings/')
        .then((res) => {setAllPostings(res.data)})
        .catch((err) => console.log(err))
    }

    const updatePostingCall = async (e) =>{
        e.preventDefault()
        try{
        await axios.put('http://localhost:8000/api/postings/2/', updatePost)
        }
        catch(err){
            console.log(err)
        }
    }
    const handleUpdateInput = (e) => {
        e.preventDefault()
        const postingUpdateInput = {...updatePost};
        postingUpdateInput[e.target.name] = e.target.value;
        setUpdatePost(postingUpdateInput)
        console.log(updatePost)
    }
useEffect(() => {
    getAllPostings()
    
}, []);

console.log(allPostings)

if(allPostings === undefined) return;

    let listOfPosting = allPostings.map((post, key) => {
        return(
            <div>
                <li>{post.title}</li>
                <li>{post.posted}</li>
            </div>
    )
})

  return (
    <div>
        <form onSubmit={updatePostingCall}>
            <input placeholder='title' name='title' value={updatePost.title} onChange={handleUpdateInput}/>
            <input placeholder='company' name='company' value={updatePost.company} onChange={handleUpdateInput}/>
            <input placeholder='posted' name='posted' value={updatePost.posted} onChange={handleUpdateInput}/>
            <input placeholder='url' name='url' value={updatePost.url} onChange={handleUpdateInput}/>
            <button>Submit</button>
        </form>
        
        {listOfPosting}
    </div>
  )
}

export default MainHub