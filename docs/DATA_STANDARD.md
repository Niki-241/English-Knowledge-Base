# English Knowledge Base Data Standard

Version: v1.0

This document defines the unified data structure for all vocabulary datasets in this repository.

---

# Field Definition

| Field | Type | Required | Example | Description |
|------|------|----------|---------|-------------|
| id | Integer | Yes | 1 | Unique vocabulary ID |
| word | String | Yes | abandon | English word |
| lemma | String | Yes | abandon | Base form of the word |
| phonetic | String | Yes | /əˈbændən/ | IPA pronunciation |
| part_of_speech | String | Yes | verb | Part of speech |
| chinese_meaning | String | Yes | 放弃 | Chinese meaning |
| english_definition | String | Yes | to leave something permanently | English definition |
| example_sentence | String | Yes | He abandoned the project. | Example sentence |
| example_translation | String | No | 他放弃了这个项目。 | Chinese translation of example |
| level | String | Yes | CET6 | Vocabulary level |
| frequency | String | Yes | A | Frequency level |
| difficulty | Integer | No | 3 | Difficulty score (1–5) |
| topic | String | No | Education | Topic category |
| synonyms | String | No | quit;leave | Synonyms (semicolon separated) |
| antonyms | String | No | continue | Antonyms |
| collocations | String | No | abandon hope | Common collocations |
| word_family | String | No | abandonment;abandoned | Word family |
| root_affix | String | No | aban- | Root / Prefix / Suffix |
| source | String | No | Original | Data source |
| tags | String | No | CET6;IELTS | Custom tags |
| status | String | Yes | learning | learning / review / mastered |
| created_at | Date | Yes | 2026-07-30 | Creation date |
| updated_at | Date | Yes | 2026-07-30 | Last update |

---

# Vocabulary Level

| Value | Description |
|------|-------------|
| CET4 | College English Test Band 4 |
| CET6 | College English Test Band 6 |
| IELTS | IELTS |
| TOEFL | TOEFL |
| GRE | GRE |
| Business | Business English |

---

# Frequency Level

| Value | Description |
|------|-------------|
| S | Super High Frequency |
| A | High Frequency |
| B | Medium Frequency |
| C | Low Frequency |

---

# Learning Status

| Value | Description |
|------|-------------|
| new | Not learned |
| learning | Currently learning |
| review | Need review |
| mastered | Fully mastered |

---

# Data Rules

1. One row represents one vocabulary item.
2. UTF-8 encoding.
3. CSV delimiter: comma (,).
4. IPA must follow the International Phonetic Alphabet.
5. Multiple values use semicolons (;).
6. No duplicate IDs.
7. No duplicate words.
8. Example sentences should be original whenever possible.

---

# Example

| id | word | phonetic | part_of_speech | chinese_meaning | level |
|----|------|-----------|----------------|-----------------|-------|
| 1 | abandon | /əˈbændən/ | verb | 放弃 | CET6 |
