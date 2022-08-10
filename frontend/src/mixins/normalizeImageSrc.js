export default {
  methods: {
    normalizeImageSrc(url) {
      if (!url) return url
      if (url.startsWith('http://localhost')) {
        return url.split('//localhost')[1]
      }
      return url
    }
  }
}
