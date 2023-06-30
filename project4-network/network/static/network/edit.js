document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll(".butt").forEach(b => b.addEventListener("click", editPost));
    document.querySelectorAll(".img").forEach(i => i.addEventListener("click", like));

});
function like(i){
    const image = i.target;
    const div = image.parentElement;
    const like = div.querySelector('p');
    
    const id = image.id;

    image.src = image.src === 'https://cdn-icons-png.flaticon.com/512/25/25423.png'
    ? 'https://cdn-icons-png.flaticon.com/512/25/25297.png'
    : 'https://cdn-icons-png.flaticon.com/512/25/25423.png';
        fetch(`/likes/${id}`)
        .then(response => response.json())
        .then(post => {
            like.innerHTML = post.likes;
        
    });
    
}  

function editPost(b){
    
        //console.log(b.target)
        const butt = b.target
        
            let id = butt.getAttribute('data-id');
            document.querySelectorAll(".butt").forEach(b => b.disabled=true);
            //console.log(id);
            fetch(`/editPost/${id}`)
        
            .then(response => response.json())
            .then(post => {
                // Print posts
                //console.log(post);

           
            const x = butt.parentElement;
            const t = x.querySelector('.postcontent');
            const postcont = t.innerHTML;

            //console.log(postcont);
            textArea = document.createElement('textarea');
            
            textArea.setAttribute("class", "form-control");
            textArea.setAttribute("required", "");
            t.replaceWith(textArea);
            //console.log(t)
            x.querySelector('textarea').innerHTML = postcont;
            newbutt = document.createElement('input');
            newbutt.setAttribute("class", "btn btn-dark butt save");
            newbutt.setAttribute("id", id);
            newbutt.setAttribute("type", "button");
            newbutt.setAttribute("value", "Save");
            
            //thisbutt = butt[i];
            butt.replaceWith(newbutt)
            //butt[i].setAttribute("value", "Save");
            if (newbutt.id == id){
            newbutt.onclick = () =>{
               
                newpost = x.querySelector('textarea').value;
                //console.log(newpost)
                if (newpost.length < 1){
                    window.alert ("Post can't be empty");
                    return true;
                }
                textArea.replaceWith(t);
                t.innerHTML = newpost;
                
                fetch(`/editPost/${id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        post: newpost
                    })   
                })
                //document.querySelectorAll('.save').forEach(s =>s.replaceWith(butt));
                newbutt.replaceWith(butt);
                document.querySelectorAll(".butt").forEach(b => b.disabled=false);
                //return false;
            }
        }
    });
    return false;       
}



