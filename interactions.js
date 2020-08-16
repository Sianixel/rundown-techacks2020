// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("helpButton");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

btn.addEventListener("click", ev => {
  modal.style.display = "block";
});

document.getElementById("form").addEventListener("submit", (event) => {
  event.preventDefault();
  let text = document.getElementById("textField");
  console.log(text.value); //take text.value to retrieve what was in the textbox
  document.getElementById("listTable").style.display = "block";

  
  let table = document.getElementById("table");
  let tbody = document.getElementById("tableBody");
  
  while(tbody.rows.length > 0) {
    tbody.deleteRow(0);
  }
  
  if (text.value === "African Giraffe Dietary Habits") {
    var urls = ["https://www.sciencedirect.com/science/article/abs/pii/0016703784900917", 
                "https://www.sciencedirect.com/science/article/abs/pii/030544039090007R", 
                "https://link.springer.com/chapter/10.1007/978-3-662-02894-0_1", 
                "https://www.nrcresearchpress.com/doi/abs/10.1139/Z99-165#.Xzir2uhKhPY", 
                "https://www.sciencedirect.com/science/article/abs/pii/0305440389900241"];
    var urls2 = ["https://journals.co.za/content/sajsci/74/8/AJA00382353_9939",
                "https://inis.iaea.org/search/search.aspx?orig_q=RN:19035123",
                "https://link.springer.com/article/10.1007/BF00347911",
                "https://www.sciencedirect.com/science/article/abs/pii/0016703787901517",
                "https://ci.nii.ac.jp/naid/10003980256/"]
    
    for (var i = 0; i < urls.length; i++) {
      var row = tbody.insertRow();
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      
      cell1.innerText = urls[i];
      cell2.innertext = urls2[i];
    }
  } else {
    for(var i = 0; i < 5; i++) {
      var row = tbody.insertRow();
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);

      cell1.innerText = "";
      cell2.innerText = "";
      cell3.innerText = Math.random();
    }
  }
  
  text.value = "";
});