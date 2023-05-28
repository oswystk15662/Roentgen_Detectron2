# import some common libraries
import numpy as np
import os, cv2
from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

#!wget http://images.cocodataset.org/val2017/000000439715.jpg -q -O coco_input.jpg こういうのは主導ダウンロード...
img = cv2.imread("./coco_input.jpg")
cv2_imshow(img)

### ObjectDetection ###

#Detectron2にはデフォルトの設定があるので，変更が必要なところだけ変更をします．
#ここで事前学習済みファイルを読み込むことで，事前学習済みモデルを使用することができます．

cfg = get_cfg() # Detectron2のデフォルトの設定ファイルをコピー
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")) # Faster R-CNNの事前学習済みモデル(のチェックポイント)と，モデル固有の設定ファイルを読み込み
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7 # 出力するbounding boxのスコアの閾値を設定

predictor = DefaultPredictor(cfg) # simple detection class
outputs = predictor(img) # ["instances"]を最後に付けると、Instance SegmentationとKeypoint Segmentationが出来る。["panoptic_seg"]をつけると名前通りのことが出来る

#推論結果が格納されているoutputsの中身を確認していきましょう． 以下のリンク先のドキュメントには，outputsの形式が示されています．細かい形式を確認したい人は公式ドキュメントを確認してみてください．

#outputsの型とkeyを確認
#outputsは辞書型となっています．今回のFaster R-CNNの推論結果ではinstancesのkeyのみ入ってることが確認できます．
print(type(outputs) + "\n" + outputs.keys())

#インスタンスの中身を確認
#outputs["instances"]の中身を確認してみます． Instancesというクラスになっており，fieldsのところに
#pred_boxes: 推論したインスタンスのbounding box
#scores: 推論したインスタンスのスコア
#pred_classes: 推論したインスタンスのクラス
#が入っていることが確認できます． (参考: Instancesクラスのドキュメント)

instances = outputs["instances"]
#instances ->   num_instances, image_height, image_width , 
#               fields = [ pred_boxes : Boxes( tensor( [[], ...], device='cuda:0' ) ), scores : tensor( [float, ...], device='cuda:0' ), pred_classes : tensor([int, ...], device='cuda:0') ]

#Visualizerクラスによる推論結果の可視化
"""
metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
vis = Visualizer(img[:,:,::-1], metadata)
out = vis.draw_instance_predictions(instances.to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])
"""

#confident_detections = instances[instances.scores >= 0.95] #スコアが0.95以上の検出結果のみ可視化
"""
vis = Visualizer(img[:,:,::-1],MetadataCatalog.get(cfg.DATASETS.TRAIN[0]))
out = vis.draw_instance_predictions(confident_detections.to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])
"""

#馬の検出結果のみ可視化
"""
thing_classes = metadata.get("thing_classes")
horse_class = thing_classes.index("horse")
horse_detections = instances[instances.pred_classes == horse_class]

vis = Visualizer(img[:,:,::-1],MetadataCatalog.get(cfg.DATASETS.TRAIN[0]))
out = vis.draw_instance_predictions(horse_detections.to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])
"""

### Instance Segmentation ###

# 推論用のcondigを設定
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7

# 推論の実行
predictor = DefaultPredictor(cfg)
instances = predictor(img)["instances"]

# 推論結果の確認
#instances

#Instancesのfieldsの中身は，次のようになっています．
#Object Detectionと同様
#・pred_boxes
#・scores
#・pred_classes
#Instance Segmentationで新たに追加
#・pred_masks: 推論したインスタンスの，画像全体に対してのマスク
#新たに追加されたpred_masksの可視化をしてみましょう．

# 馬のインスタンスから，馬のmaskを取得
thing_classes = metadata.get("thing_classes")
horse_class = thing_classes.index("horse")
horse_detections = instances[instances.pred_classes == horse_class]
horse_mask = horse_detections.get("pred_masks")

cv2_imshow(horse_mask[0].cpu().numpy().copy() * 255)

#推論結果の可視化
metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
vis = Visualizer(img[:,:,::-1], metadata)
out = vis.draw_instance_predictions(instances.to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])