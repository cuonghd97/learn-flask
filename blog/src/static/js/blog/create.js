$(document).ready(function() {
    var formData = new FormData()
    var title = formData.append("title", $("#title").val())
    var content = formData.append("content", $("#content").val())
})