import {TeX} from "./math_text"
import {isString} from "core/util/types"
import {BaseText} from "./base_text"

export function is_tex_string(text: unknown): boolean {
  if (!isString(text)) return false

  const dollars = "^\\$\\$.*?\\$\\$$"
  const braces  = "^\\\[.*?\\\]$"
  const parens  = "^\\\(.*?\\\)$"

  // mathjax has more defaults like \begin \end, are we going to support them?
  const pat = new RegExp(`${dollars}|${braces}|${parens}`)

  return pat.test(text)
};

export function tex_from_text_like(text: string | BaseText): TeX | null {
  if (text instanceof TeX)
    return text

  if (isString(text) && is_tex_string(text))
    return new TeX({text: text.slice(2, -2)})

  return null
}