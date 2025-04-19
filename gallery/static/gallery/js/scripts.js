// gallery/static/gallery/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    window.loadProducts = function(productLineId) {
        console.log("Fetching products for product line ID:", productLineId);  // Debugging
        fetch(`/gallery/products/${productLineId}/`)
            .then(response => response.json())
            .then(data => {
                console.log("Products fetched:", data);  // Debugging
                const productsContainer = document.getElementById('products');
                productsContainer.innerHTML = '';  // Clear previous content

                data.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.classList.add('product');

                    const productImg = document.createElement('img');
                    productImg.src = product.image;
                    productImg.alt = product.name;

                    const productName = document.createElement('h5');
                    productName.textContent = product.name;

                    const productDescription = document.createElement('p');
                    productDescription.textContent = product.description;

                    const productDetails = document.createElement('p');
                    productDetails.textContent = product.details;

                    productDiv.appendChild(productImg);
                    productDiv.appendChild(productName);
                    productDiv.appendChild(productDescription);
                    productDiv.appendChild(productDetails);
                    productsContainer.appendChild(productDiv);
                });
            });
    };
});
