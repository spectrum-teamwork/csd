<template>
  <Layout>
    <template v-if="$page.news">
      <csd-news-post
        :title="$page.news.title"
        :content="$page.news.text"
        :image="$page.news.image"
      />
    </template>
  </Layout>
</template>
<page-query>
query ($newsId: ID) {
  news (id: $newsId) {
    id
    title
    text
    image
  }
}
</page-query>
<script>
import CsdNewsPost from '../../components/CsdNewsPost'

export default {
  name: 'NewsPost',
  components: { CsdNewsPost }
}
</script>
