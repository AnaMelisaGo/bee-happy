//=========================================================================
//                 MY CUSTOM DATABASE
//=========================================================================

let blogArticles = [
    {
        id: '1',
        titulo: 'Jardenería con niños',
        autor: 'AnaMelisaGo',
        resumen: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
        cuerpo: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,',
        image: 'images/gardening.jpg',
        categoria: 'jardeneria',
        fecha_publicacion: '22 Enero 2026',
    },
    {
        id: '2',
        titulo: 'Todo sobre abejas de miel',
        autor: 'AnaMelisaGo',
        resumen: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
        cuerpo: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,',
        image: 'images/bee-flower.webp',
        categoria: 'abejas',
        fecha_publicacion: '02 Febrero 2026',
    },
    {
        id: '3',
        titulo: 'La miel y sus beneficios',
        autor: 'AnaMelisaGo',
        resumen: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
        cuerpo: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,',
        image: 'images/honey-sweet.jpg',
        categoria: 'miel',
        fecha_publicacion: '10 Febrero 2026',
    },
    // {
    //     id: '4',
    //     titulo: 'Cómo construir tu "Bee Hotel" para abejas solitarias',
    //     autor: 'AnaMelisaGo',
    //     resumen: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
    //     cuerpo: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,',
    //     image: 'images/bee-hotel.webp',
    //     categoria: 'apicultura',
    //     fecha_publicacion: '22 Febrero 2026',
    // },
    // {
    //     id: '5',
    //     titulo: 'Rescatamos nuestros pequeños amigos: Las Abejas',
    //     autor: 'AnaMelisaGo',
    //     resumen: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
    //     cuerpo: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,',
    //     image: 'images/save-bees.jpg',
    //     categoria: 'rescatar',
    //     fecha_publicacion: '04 Marzo 2026',
    // },
    
];

//=========================================================================
//                  JS CODES FOR HOMEPAGE
//=========================================================================

console.log('Hello from home')
// let img = `${STATIC_URL + blogArticles[0].image}`;
// document.getElementById('img-top').src = img;
//=========================================================================
//                  JS CODES (CLASS EXERCISE)
//=========================================================================


//====================== FUNCION 1 : DIBUJAR CARDS ========================
const dibujarTarjetas = (listaPosts) => {
    let cardContenedor = document.getElementById('card-container');

    if (!cardContenedor) return;

    //limpiar contenedor
    cardContenedor.innerHTML = '';

    //Iterrar blogArticles
    listaPosts.forEach((post) => {
        let myCard = `<div class="bee-card">
            <div class="bee-card-head">
                <img src="${STATIC_URL + post.image}" class="card-img-top" alt="Imagen principal del blog">
                <div class="bee-pill">${post.categoria}</div>
            </div>
            <div class="bee-card-body">
                <h5 class="bee-card-title">${post.titulo}</h5>
                <p class="bee-card-text">${post.resumen}</p>
                <a href="/blog_post?id=${post.id}" class="btn-read">Read more <i class="fa-solid fa-arrow-right-long"></i></a>
            </div>
        </div>`;
        cardContenedor.innerHTML += myCard;
    });
};

//====================== FUNCION 2: CARGAR EL POST (pagina del post) ========================

const loadPostDetails = () => {
    let currentUrl = new URLSearchParams(window.location.search);
    let idPost = currentUrl.get('id');
    console.log(currentUrl);
    if (!idPost) return;

    let postEncontrado;
    blogArticles.forEach((item) => {
        if (item.id == idPost) {
            postEncontrado = item;
        }
    });

    if (postEncontrado) {
        document.getElementById('imagen').src = `${STATIC_URL + postEncontrado.image}`;
        console.log(postEncontrado.image);
        document.getElementById('titulo').innerText = postEncontrado.titulo;
        document.getElementById('resumen').innerText = postEncontrado.resumen;
        document.getElementById('nombre-autor').innerText = postEncontrado.autor;
        document.getElementById('fecha').innerText = postEncontrado.fecha_publicacion;
        document.getElementById('categoria-post').innerText = postEncontrado.categoria;
        document.getElementById('titulo-2').innerText = postEncontrado.titulo;
        document.getElementById('cuerpo').innerText = postEncontrado.cuerpo;
        document.getElementById('autor-aside').innerText = postEncontrado.autor;
    }

};

//====================== FUNCION 3: FILTRO DE CATEGORIAS (botones index) ========================

const filtrarPorCategoria = (categoria) => {
    if (categoria === 'todos') {
        dibujarTarjetas(blogArticles);
    } else {
        let listaFiltrada = [];
        blogArticles.forEach((p) => {
            if (p.categoria === categoria) {
                listaFiltrada.push(p);
            }
        });
        dibujarTarjetas(listaFiltrada);
    }
};


//======================  ========================

window.onload = () => {
    if (document.getElementById('card-container')) {
        dibujarTarjetas(blogArticles);
    }

    if (document.getElementById('post-content')) {
        loadPostDetails();
    }
};




