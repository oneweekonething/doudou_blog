/**
 * Created by panda on 17/10/27.
 */

function do_reply(parentid) {
    console.log(parentid);
    $("#id_parent_comment_id").val(parentid)
    $("#commentform").appendTo($("#div-comment-"+parentid))
    $("#reply-title").hide()
    $("#cancel-comment").show()

}

function cancel_reply() {
    $("#reply-title").show();
    $("#cancel_comment").hide();
    $("#id_parent_comment_id").val('')
    $("#commentform").appendTo($("#respond"));
}
