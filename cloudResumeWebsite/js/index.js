const counter = document.querySelector(".counter-number");
async function updateCounter()
{
  let response = await fetch("https://fic52a2ph2qsh5ifszkuqmko2m0qcvxr.lambda-url.eu-north-1.on.aws/");
  let data = await response.json();
  console.log(data);
  counter.innerHTML = ` Görüntülenme Sayısı: ${data}`;
}

updateCounter();