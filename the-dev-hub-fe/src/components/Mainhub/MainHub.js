import React, { useEffect } from 'react'
import axios from 'axios'

const MainHub = () => {
    const getAllPostings = () =>{
        axios
        .get('http://localhost:8000/api/postings/')
        .then((res) => {
            console.log(res)
        })
    
    }
useEffect(() => {
    getAllPostings()
}, []);
  return (
    <div>MainHub</div>
  )
}

export default MainHub