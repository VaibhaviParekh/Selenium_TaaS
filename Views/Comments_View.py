from PageObjects.Comments import CommentObjects


class CommentsView:

    def __init__(self, drv):
        # Create instance of the Comments Page Objects
        self.obj_driver = drv
        self.obj_comments = CommentObjects(drv)

    def verify_comment_added(self, comment, date):
        try:
            comment_exists = self.obj_comments.verify_comment(comment)
            if comment_exists == 1:
                print("PASS- Comment "+comment+" verified successfully")
            else:
                print("FAIL- Comment "+comment+" not verified successfully")

            comment_date_exists = self.obj_comments.verify_comment_date(comment,date)
            if comment_date_exists == 1:
                print("PASS- Comment date " + date + " verified successfully")
            else:
                print("FAIL- Comment date " + date + " not verified successfully")

        except Exception as e:
            print("Error : {}".format(e))

    def verify_no_comment(self):
        try:
            no_comment = self.obj_comments.verify_no_comments()
            if no_comment == 1:
                print("PASS- No comment instance exists.")
            else:
                print("FAIL- Comment instance is present")
        except Exception as e:
            print("Error : {}".format(e))