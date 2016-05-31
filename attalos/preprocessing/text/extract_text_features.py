from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import gzip


def extract_text_features(dataset_prep):
    """
    Extract captions and tags from dataset_prep object
    Args:
        dataset_prep: (attalos.dataset.DatasetPrep): Dataset to extract features from

    Returns:

    """
    tag_dict = {}
    caption_dict = {}
    for img_record in dataset_prep: # img_record (attalos.dataset.dataset_prep.RecordMetadata)
        id = img_record.id
        tags = img_record.tags
        captions = img_record.captions
        tag_dict[id] = tags
        caption_dict[id] = captions
    return tag_dict, caption_dict


def process_dataset(dataset_prep, output_fname):
    """
    Uses dataset_prep object to extract text features

    Args:
      dataset_prep (attalos.dataset.DatasetPrep): Dataset to convert
      output_fname: Output filename to extract to

    Returns:

    """

    tag_dict, caption_dict = extract_text_features(dataset_prep)

    output_object = {'tags': tag_dict, 'captions': caption_dict}
    if output_fname.endswith('.gz'):
        output_file = gzip.open(output_fname, 'w')
    else:
        output_file = open(output_fname, 'w')
    json.dump(output_object, output_file)


def main():
    import argparse
    from attalos.dataset.mscoco_prep import MSCOCODatasetPrep

    parser = argparse.ArgumentParser(description='Extract text features.')
    parser.add_argument('--dataset_dir',
                      dest='dataset_dir',
                      type=str,
                      help='Directory with input data')
    parser.add_argument('--output_fname',
                      dest='output_fname',
                      default='captions_text.json.gz',
                      type=str,
                      help='Output json filename')

    args = parser.parse_args()
    dataset_prep = MSCOCODatasetPrep(args.dataset_dir)
    process_dataset(dataset_prep, args.output_fname)

if __name__ == '__main__':
    main()
