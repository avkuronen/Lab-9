function deleteProduct(productId) {
  fetch(`/delete/${productId}`, { method: 'DELETE' }).then(response => {
    if (response.ok) {
      location.reload()
    }
  })
}

function addProduct(event) {
  event.preventDefault()
  let prodName = document.getElementById('hardware_part').value
  let price = document.getElementById('price').value
  fetch('/add', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      'hardware_part': prodName,
      'price': price
    })
  })
  .then(response => {
    if (response.ok) {
      location.reload()
    }
  })
}

function deleteAllProducts() {
  fetch('/delete', { method: 'DELETE' }).then(response => {
    if (response.ok) {
      location.reload()
    }
  })
}
