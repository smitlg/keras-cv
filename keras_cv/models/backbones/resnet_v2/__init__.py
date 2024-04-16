# Copyright 2023 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from keras_cv.models.backbones.resnet_v2.resnet_v2_backbone_presets import (
    backbone_presets_no_weights,
)
from keras_cv.models.backbones.resnet_v2.resnet_v2_backbone_presets import (
    backbone_presets_with_weights,
)
from keras_cv.models.backbones.resnet_v2.resnet_v2_backbone import (
    ResNetV2Backbone,
)
from keras_cv.models.backbones.resnet_v2.resnet_v2_aliases import (
    ResNet50V2Backbone,
)
from keras_cv.utils.preset_utils import register_presets, register_preset

register_presets(backbone_presets_no_weights, (ResNetV2Backbone, ), with_weights=False)
register_presets(backbone_presets_with_weights, (ResNetV2Backbone, ), with_weights=True)
register_preset("resnet50_v2_imagenet", backbone_presets_with_weights["resnet50_v2_imagenet"],
                (ResNet50V2Backbone,), with_weights=True)
