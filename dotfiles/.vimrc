"color scheme
colors desert
syntax on

"syntax highlighting refresh
noremap <F12> <Esc>:syntax sync fromstart<CR>
inoremap <F12> <C-o>:syntax sync fromstart<CR>

"1 tab = 2 spaces
set shiftwidth=2
set tabstop=2 
set autoindent
filetype plugin indent on

"iff uppercase
set ignorecase
set smartcase

"normal backspace
set backspace=indent,eol,start

"line numbers
set ruler

"vertical windows
noremap <F2> :windo wincmd K<CR>
"horizontal windows
noremap <F3> :windo wincmd H<CR>

"cursor type - block all
set guicursor=a:block-Cursor

"Defaul for NERDTree
"autocmd VimEnter * NERDTree C:/
nmap <C-q> :NERDTreeToggle<CR>

let NERDTreeMinimalUI=1 
let NERDTreeDirArrows=1

"NERDTree needs this
set nocompatible

"no sound on errors
set noerrorbells
set novisualbell
set vb t_vb=

"no toolbar
set guioptions=egmrLt

"no highlight
set nohlsearch

"init matchit
runtime macros/matchit.vim

"turn off blinking cursor
:set guicursor+=a:blinkon0

" disable arrow keys
map <up> <nop>
map <down> <nop>
map <left> <nop>
map <right> <nop>
imap <up> <nop>
imap <down> <nop>
imap <left> <nop>
imap <right> <nop>
