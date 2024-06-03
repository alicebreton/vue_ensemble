import spacy
import glob
import argparse
import sys

nlp_trf = spacy.load("fr_core_news_lg")

def calcul_means(file_path):
    
    with open(file_path, "r") as file:
        text = file.read().replace("\n", " ")

    doc = nlp_trf(text)
    
    total_verbs = 0
    total_sentences = 0
    total_words = 0

    for sent in doc.sents:
        total_sentences += 1

        verbs_in_sentence = sum(1 for token in sent if token.pos_ == "VERB")
        words_in_sentence = sum(1 for token in sent if token.text != "")
        total_verbs += verbs_in_sentence
        total_words += words_in_sentence

    return text,"total P: ",total_sentences, "total V: ", total_verbs,"total T: ", total_words

def main(args):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input_path', help="Path to the data dir")
    parser.add_argument('--output_text', help="Path to output data.", default = "./vue_ensemble/output.txt")

    opt = parser.parse_args(args)

    input_folder = opt.input_path
    output_file = opt.output_text

    list_files = glob.glob(str(input_folder)+"*.txt")

    with open(output_file, "w") as f:
        for file in list_files:
            f.write(str(file)+str(calcul_means(file))+"\n")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

