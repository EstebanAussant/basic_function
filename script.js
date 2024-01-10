async function  remplir_accessoires(){

    const reponse =  await fetch('accessoires.json');
    const JSON = await reponse.json();  
   

    let template = document.querySelector("#template_accessoires"); 
    
    for (const a of JSON.tableau_accessoires) {
            let clone = document.importNode(template.content, true);

            newContent = clone.firstElementChild.innerHTML
            .replace(/{{accessoires-titre}}/g, a.titre)
            .replace(/{{accessoires-texte}}/g, a.texte)
            .replace(/{{accessoires-image}}/g, a.image)

            clone.firstElementChild.innerHTML = newContent;      
            document.getElementById('grid-container').appendChild(clone);
    }   
}

remplir_accessoires()