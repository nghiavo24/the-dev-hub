import React, { useEffect, useState } from 'react'
import axios from 'axios'

const MainHub = () => {
    const [allPostings, setAllPostings] = useState()

    const getAllPostings = (e) =>{
        axios
        .get('http://localhost:8000/api/postings/')
        .then((res) => {setAllPostings(res.data)})
        .catch()
    }
console.log(allPostings)

    
useEffect(() => {
    getAllPostings()
    
}, []);

if(allPostings === undefined) return;

    let listOfPosting = allPostings.map((post, key) => {
        return(
        <li>{post.title}</li>
    )
})

  return (
    <div>{listOfPosting}</div>
  )
}

export default MainHub