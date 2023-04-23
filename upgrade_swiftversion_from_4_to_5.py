import os
import re

if __name__ == '__main__':
    root_path = "your_project_path"
    # use a key-value map to store the replaced code.Key is the code will be replaced, Value is the new code.
    # it also supports regex expression, e.g:"sendSubview(\s*toBack:\s*":'sendSubviewToBack\('. you can also add some missed replaced code.
    # all these api code should be replaced come from the XCode prompt.
    replacedAPI = {
        "kCAMediaTimingFunctionEaseInEaseOut":"CAMediaTimingFunctionName.easeInEaseOut",
        "kCAMediaTimingFunctionEaseOut":"CAMediaTimingFunctionName.easeOut",
        "UITableViewCellSeparatorStyle":"UITableViewCell.SeparatorStyle",
        "kCAMediaTimingFunctionLinear":"CAMediaTimingFunctionName.linear",
        "UITableViewCellStyle":"UITableViewCell.Style",
        "NSUnderlineStyle.styleSingle.rawValue":"NSUnderlineStyle.single.rawValue",
        "bringSubview(\s*toFront:\s*":'bringSubviewToFront\(',
        "sendSubview(\s*toBack:\s*":'sendSubviewToBack\(',
        "AVAudioSessionCategoryPlayAndRecord":'AVAudioSession.Category.playAndRecord',
        "UIApplicationOpenSettingsURLString":"UIApplication.openSettingsURLString",
        "UITableViewCell.Style":"UITableViewCell.CellStyle",
        "NSAttributedStringKey":"NSAttributedString.Key",
        "kCATransitionFade":"CATransitionType.fade",
        "kCAFillRuleEvenOdd":"CAShapeLayerFillRule.evenOdd",
        "UIViewContentMode":"UIView.ContentMode",
        "RunLoopMode.commonModes":"RunLoop.Mode.common",
        "UIGestureRecognizerState":"UIGestureRecognizer.State",
        ".defaultRunLoopMode":"RunLoop.Mode.default",
        "kCAGravityResizeAspectFill":"CALayerContentsGravity.resizeAspectFill",
        "addChildViewController":"addChild",
        "UIControlState":"UIControl.State",
        "UIControlEvents":"UIControl.Event",
        "UIButtonType":"UIButton.ButtonType",
        "kCAFillModeForwards":"CAMediaTimingFillMode.forwards",
        "UITableViewCellSelectionStyle":"UITableViewCell.SelectionStyle",
        "UICollectionElementKindSectionHeader":"UICollectionView.elementKindSectionHeader",
        "UITextFieldViewMode":"UITextField.ViewMode",
        "removeFromParentViewController":"removeFromParent",
        "UIApplicationOpenURLOptionsKey":"UIApplication.OpenURLOptionsKey",
        "UIApplicationState":"UIApplication.State",
        "UIWindowLevelStatusBar":"UIWindow.Level.statusBar",
        "Notification.Name.UIKeyboardWillShow":"UIResponder.keyboardWillShowNotification",
        "Notification.Name.UIKeyboardWillHide":"UIResponder.keyboardWillHideNotification",
        "UIKeyboardFrameEndUserInfoKey":"UIResponder.keyboardFrameEndUserInfoKey",
        "AVAudioSessionCategoryPlayback":"AVAudioSession.Category.playback",
        "NSNotification.Name.UIApplicationDidEnterBackground":"UIApplication.didEnterBackgroundNotification",
        "NSNotification.Name.UIApplicationWillEnterForeground":"UIApplication.willEnterForegroundNotification",
        "kCALineCapRound":"CAShapeLayerLineCap.round",
        ".UIApplicationWillResignActive":"UIApplication.willResignActiveNotification",
        ".UIApplicationDidBecomeActive":"UIApplication.didBecomeActiveNotification",
        "kCALineJoinRound":"CAShapeLayerLineJoin.round",
    }
    # Get all the files in the directory
    g = os.walk(root_path)
    for path, dir_list, file_list in g:
        for file in file_list:
            if file.endswith('.swift'):
                print(file)
                for key in replacedAPI :
                    # 使用sed命令进行替换 sed -i 's/原字符串/替换字符串/g' filename
                    absolutFilePath = os.path.join(path, file)
                    replaceCommand = " sed -i \"\" 's/%s/%s/g' %s" % (key, replacedAPI[key], absolutFilePath)
                    os.system(replaceCommand)
                    print("command: %s" % replaceCommand)

    