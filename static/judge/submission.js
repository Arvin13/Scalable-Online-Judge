document.getElementById('input-code').addEventListener('keydown', function(e) {
    if (e.key == 'Tab') {
      e.preventDefault();
      var start = this.selectionStart;
      var end = this.selectionEnd;
  
      // set textarea value to: text before caret + tab + text after caret
      this.value = this.value.substring(0, start) +
        "\t" + this.value.substring(end);
  
      // put caret at right position again
      this.selectionStart =
        this.selectionEnd = start + 1;
    }
  });



$('#plang').change(function() {
    var mylist = document.getElementById("plang");
    value = mylist.options[mylist.selectedIndex].text;
    $('#val').text = value;
    let div1 = document.getElementById('python-text');
    let div2 = document.getElementById('clang-text');
    let div3 = document.getElementById('cpp-text');
    let div4 = document.getElementById('java-text');
    if (value == 'Python') {
      div1.style.display="block";
      div2.style.display="none";
      div3.style.display="none";
      div4.style.display="none";
    } else if (value == 'Clang') {
        div2.style.display="block";
        div1.style.display="none";
        div3.style.display="none";
        div4.style.display="none";
    } else if (value == 'C++') {
        div3.style.display="block";
        div1.style.display="none";
        div2.style.display="none";
        div4.style.display="none";
    } else if (value == 'Java') {
        div4.style.display="block";
        div1.style.display="none";
        div2.style.display="none";
        div3.style.display="none";
    } 
});

$("#input-file").change(function(){
    var new_file_name = $('#input-file')[0].files[0].name;
    document.getElementById('input-file-label').innerHTML= new_file_name;
  });