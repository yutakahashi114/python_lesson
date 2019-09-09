FROM python:3.7.0

RUN apt-get update \
 && apt-get install -y \
    git \
    unzip \
    vim \
 && pip install \
    --upgrade pip \
    cirq \
    matplotlib==2.2.2 \
    sympy \
    matplotlib_venn \
    beautifulsoup4==4.6.0 \
    gspread \
    oauth2client \
    selenium

WORKDIR /usr/share/fonts
ENV RICTY_DIMINISHED_VERSION 3.2.4
ADD https://github.com/mzyy94/RictyDiminished-for-Powerline/archive/$RICTY_DIMINISHED_VERSION-powerline-early-2016.zip .
RUN unzip -jo $RICTY_DIMINISHED_VERSION-powerline-early-2016.zip \
    && fc-cache -fv

WORKDIR /usr/local/lib/python3.7/site-packages/matplotlib/mpl-data
RUN rm -f matplotlibrc \
 && echo "backend : Agg" >> matplotlibrc \
 && echo "font.family : Ricty Diminished" >> matplotlibrc

WORKDIR /usr/local/src
