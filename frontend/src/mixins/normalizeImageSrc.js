export default {
  methods: {
    normalizeImageSrc(url) {
      if (!url) return url
      if (url.startsWith('http://backend')) {
        return url.split('//backend')[1]
      }
      return url
    }
  }
}
