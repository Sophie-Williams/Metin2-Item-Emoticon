## 1.) Find this:
		self.defFontName = localeInfo.UI_DEF_FONT

## 2.) Add after this:
		if app.ENABLE_ITEM_EMOTION:
			self.EmoticonKeyBoard		= None
			self.EmoticonKeyText		= None

## 1.) Find this:
	def ClearToolTip(self):
		self.toolTipHeight = 12
		self.childrenList = []

## 2.) Add after this:
		if app.ENABLE_ITEM_EMOTION:
			if self.EmoticonKeyBoard:
				self.EmoticonKeyBoard.Hide()

## 1.) Find this:
class ItemToolTip(ToolTip):

## 2.) Add after this:
	if app.ENABLE_ITEM_EMOTION:
		EmoticonKeyBoard		= None
		EmoticonKeyText			= None


## 1.) Find this:
		self.ShowToolTip()

	def __DragonSoulInfoString (self, dwVnum):

## 2.) Add before this (self.ShowToolTip()):
		if app.ENABLE_ITEM_EMOTION:
			self.EmoticonToolTip(itemVnum)

## 1.) Find this:
	def __AdjustMaxWidth(self, attrSlot, desc):
		....

## 2.) Add before this:
	if app.ENABLE_ITEM_EMOTION:
		def EmoticonToolTip(self, itemVnum):
			def EmoticonLine(i):
				_Vali_ = "|E%s|e"
				return _Vali_ % (i)

			self.EmoticonKeyBoard = ui.ThinBoard()
			self.EmoticonKeyBoard.SetParent(self)
			self.EmoticonKeyBoard.SetSize(150, 25)

			self.EmoticonKeyText = ui.TextLine()
			self.EmoticonKeyText.SetParent(self.EmoticonKeyBoard)
			self.EmoticonKeyText.SetPackedFontColor(grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0))

			self.EMOTICON_MAX	= 10
			self.ItemDict		= {}
			self.ItemDict["ItemVnums"]	= [10,20,30,40,50,60,70,80,90,100]

			self.DescDict = {
				'emo_0' : localeInfo.EMOTICON_TOOLTIP_UPSET,
				'emo_1' : localeInfo.EMOTICON_TOOLTIP_CRYING,
				'emo_2' : localeInfo.EMOTICON_TOOLTIP_FROWNY,
				'emo_3' : localeInfo.EMOTICON_TOOLTIP_SQUINT,
				'emo_4' : localeInfo.EMOTICON_TOOLTIP_UNSURE,
				'emo_5' : localeInfo.EMOTICON_TOOLTIP_SHOCKED,
				'emo_6' : localeInfo.EMOTICON_TOOLTIP_GASP,
				'emo_7' : localeInfo.EMOTICON_TOOLTIP_WINKING,
				'emo_8' : localeInfo.EMOTICON_TOOLTIP_TONGUEOUT,
				'emo_9' : localeInfo.EMOTICON_TOOLTIP_DEVIL}

			for iEmoticon in xrange(self.EMOTICON_MAX):
				for i in xrange(len(self.ItemDict["ItemVnums"])):
					_Tokens_, _Index_, _Iterator_ = self.ItemDict["ItemVnums"][i], str(itemVnum)[-1:], str(iEmoticon)
					_Valiant_ = (_Tokens_ <= itemVnum and itemVnum <= _Tokens_ + self.EMOTICON_MAX-1) and (_Index_ == _Iterator_)
					SpaceInfo	= ' '

					EmoText		= self.DescDict['emo_%d' % iEmoticon]
					EmoImg		= SpaceInfo+EmoticonLine("emoji/emo_%d" % (int(iEmoticon)))

					if (_Valiant_):
						self.EmoticonKeyText.SetText(EmoText+EmoImg)
						self.EmoticonKeyText.SetPosition(80, 10)
						self.EmoticonKeyText.SetHorizontalAlignCenter()

						self.ValiantHeight = +15
						self.EmoticonKeyBoard.SetPosition(self.toolTipWidth/2-75, self.toolTipHeight+self.ValiantHeight)
						self.ValiantHeight += self.EmoticonKeyBoard.GetHeight()

						self.childrenList.append(self.EmoticonKeyText)
						self.childrenList.append(self.EmoticonKeyBoard)
						self.EmoticonKeyBoard.Show()
						self.EmoticonKeyText.Show()
						self.ResizeToolTip()

